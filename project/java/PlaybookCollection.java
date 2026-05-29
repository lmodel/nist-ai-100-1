package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A container for a set of PlaybookEntry instances - the
serialisation root for an AI RMF Playbook companion document.
Validate with ``linkml-validate --target-class PlaybookCollection``;
the canonical tree-root for the schema is ``AiRmfFramework``.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PlaybookCollection  {

  private List<PlaybookEntry> entries;


}